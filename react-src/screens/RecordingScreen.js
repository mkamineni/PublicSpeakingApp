import React, { Component } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Alert, CameraRoll } from 'react-native';
import { Camera, Permissions } from 'expo';
import { RNS3 } from 'react-native-aws3';
import { AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY } from '../secret';


export default class RecordingScreen extends Component {
    constructor(props){
        super(props);
        this.state = {
            hasCameraPermission: null,
            hasAudioPermission: null,
            isRecording: false,
            fileUrl: null,
            isDoneRecording: false,
            loading: '',
            msg: '',
            data: [],
        };
    }
    
    async componentWillMount() {
        const { status } = await Permissions.askAsync(Permissions.CAMERA, Permissions.AUDIO_RECORDING);
        console.log(status);
        this.setState({
            hasVideoPermission: status === 'granted',
            isRecording: false,
            fileUrl: null,
        });
    }

    uploadVideo(fileUrl) {
        const file = {
            uri: fileUrl,
            name: "speech.mov",
            type: "mov"
        }

        const options = {
            keyPrefix: "uploads/",
            bucket: "public-speech",
            region: "us-east-1",
            accessKey: AWS_ACCESS_KEY_ID,
            secretKey: AWS_SECRET_ACCESS_KEY,
            successActionStatus: 201
        }

        RNS3.put(file, options).then(response => {
        if (response.status !== 201)
            throw new Error(response.status);
        else{
            console.log(response.body.postResponse.location);
            this.analyzeVideo(response.body.postResponse.location);
        }
        /**
         * {
         *   postResponse: {
         *     bucket: "your-bucket",
         *     etag : "9f620878e06d28774406017480a59fd4",
         *     key: "uploads/image.png",
         *     location: "https://your-bucket.s3.amazonaws.com/uploads%2Fimage.png"
         *   }
         * }
         */
        });
    }

    analyzeVideo(fileUrl) {
        this.setState({ loading: 'analyzeVideo'}); //check the loading prop in lower components, if its not an empty string display a loading circle
        const body = { form: fileUrl };
        console.log(fileUrl, body, JSON.stringify(body))
        fetch(`http://juicy.local:5000/analyze/`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body),
        })
            .then(res => {
                console.log(res);
                console.log(obj[0], obj[1], obj[2]);
                res = res.json();
                const data = obj[0]; //depends on what we want to display first, we are returned len3 tuple
                this.setState({
                    loading: '',
                    msg: 'Video analyzed',
                    data: [ data ]
                });
                console.log('video analyzed');
                },
                error => {
                    this.setState({
                        loading: '', 
                        msg: 'Error analyzing video'
                    });
                    console.log('ERROR:');
                    console.error(error);
                }
            );
    }

    handleData = { //contains functions, maybe like retrieveGraph or something
        uploadVideo: this.uploadVideo
    }

    onStartRecording = async () => {
        if (this.camera) {
          this.setState({ isRecording: true, fileUrl: null });
          this.camera.recordAsync({ quality: '4:3' })
            .then((file) => {
              this.setState({ fileUrl: file.uri});
              CameraRoll.saveToCameraRoll(file.uri, "video");
              this.uploadVideo(file.uri);
            });
        }
    }

    onStopRecording = () => {
        this.camera.stopRecording();
        this.setState({ isDoneRecording: true, isRecording: false });
    };

    render() {
        const { hasVideoPermission} = this.state;
        const { navigate } = this.props.navigation;
        const styles = StyleSheet.create({
            container: {
                flex: 1,
                backgroundColor: '#78a6f2'
            },
            text: {
                fontFamily: 'latoBold',
                color: 'white',
            },
            footer: {
                height: 85,
                flexDirection: 'row',
                backgroundColor: '#78a6f299',
            }
        });

        if (hasVideoPermission == null) {
            return <View style={styles.container} />;
        } else if (hasVideoPermission === false) {
            console.log(this.state);
            Alert.alert(
                'Permissions',
                'Please go to Settings and allow the app to use the camera and microphone.',
                [
                    {text: 'Cancel', onPress: () => navigate('Start')},
                    {text: 'OK', onPress: () => navigate('Start')},
                ],
                { cancelable: false }
            );
            return (
                <View style={styles.container} />
            );
        } else {
            return(
                <View style={styles.container}>
                    <Camera
                        style={{ flex: 1 }}
                        type={Camera.Constants.Type.front}
                        ref={ref => { this.camera = ref; }}
                    >
                        <TouchableOpacity
                            style={[styles.footer, {backgroundColor: `${this.state.isRecording ? '#ee000099' : '#78a6f299'}`}]}
                            onPress={() => this.state.isRecording ? this.onStopRecording() : this.onStartRecording()}
                        >

                        </TouchableOpacity>
                    </Camera>
                </View>
            );
        }
    }
}