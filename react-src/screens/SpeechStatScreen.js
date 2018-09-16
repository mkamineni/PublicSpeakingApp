import React, { Component } from 'react'
import { ScrollView, View, Text, StyleSheet, TouchableOpacity } from 'react-native'

export default class SpeechStatScreen extends Component {
    constructor(props){
        super(props);
        this.state = {
            loading: '',
            msg: '',
            data: [],
        };
    }
    componentDidMount() {
        this.setState({
            data: [this.props.navigation.getParam("screenData", [])]
        })
    }
    render() {
        const styles = StyleSheet.create({
            scrollContainer: {
                backgroundColor: '#78a6f2'
            },
            text: {
                fontFamily: 'latoLight',
                color: 'white',
                fontSize: 20,
                margin: 10,
            },
            label: {
                fontSize: 20,
                color: '#78a6f2',
                fontFamily: 'latoRegular',
            },
            button: {
                backgroundColor: '#fff8',
                borderRadius: 5,
                padding: 15,
            },
        });
        const { navigate } = this.props.navigation;
        const speechStatData = this.props.navigation.getParam("screenData", "")[1];
        return(
            <ScrollView style ={styles.scrollContainer}>
                <Text style={styles.text}>
                    {speechStatData}
                </Text>
                <TouchableOpacity
                    onPress={() => navigate('Recording')}
                    style={styles.button}
                >
                    <Text style={styles.label}>next!</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    onPress={() => navigate.goBack()}
                    style={styles.button}
                >
                    <Text style={styles.label}>back!</Text>
                </TouchableOpacity>
            </ScrollView>
        )
    }
}