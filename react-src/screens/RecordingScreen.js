import React, { Component } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Alert, CameraRoll } from 'react-native';
import { Camera, Permissions } from 'expo';

export default class RecordingScreen extends Component {
    constructor(props){
        super(props);
        this.state = {
            hasCameraPermission: null,
            hasAudioPermission: null,
            isRecording: false,
            fileUrl: null,
            isDoneRecording: false,
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

    onStartRecording = async () => {
        if (this.camera) {
          this.setState({ isRecording: true, fileUrl: null });
          this.camera.recordAsync({ quality: '4:3' })
            .then((file) => {
              this.setState({ fileUrl: file.uri});
              CameraRoll.saveToCameraRoll(file.uri, "video");
            })
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