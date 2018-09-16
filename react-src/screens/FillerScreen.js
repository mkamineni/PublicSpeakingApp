import React, { Component } from 'react'
import { ScrollView, View, Text, StyleSheet, TouchableOpacity } from 'react-native'

export default class FillerScreen extends Component {
    constructor(props){
        super(props);
        this.state = {
            loading: '',
            msg: '',
            data: [], //initialize data here from params
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
                marginTop: 80,
                backgroundColor: '#fff8',
                borderRadius: 5,
                padding: 15,
            },
        });
        const { navigate } = this.props.navigation;
        const fillerData = this.props.navigation.getParam("screenData", "")[0];
        return(
            <ScrollView style ={styles.scrollContainer}>
                <Text style={styles.text}>
                    {fillerData}
                </Text>
                <TouchableOpacity
                    onPress={() => navigate('SpeechStat'), {screenData: this.state.data}}
                    style={styles.button}
                >
                <Text style={styles.label}>View speech statistics!</Text>
                </TouchableOpacity>
            </ScrollView>
        )
    }
}