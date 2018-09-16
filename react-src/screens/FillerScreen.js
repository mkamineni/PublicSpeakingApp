import React, { Component } from 'react'
import { ScrollView, View, Text, StyleSheet, TouchableOpacity } from 'react-native'

export default class FillerScreen extends Component {
    constructor(props){
        super(props);
        this.state = {
            loading: '',
            msg: '',
            data: [],
        };
    }
    render() {
        const styles = StyleSheet.create({
            container: {
                alignItems: 'center',
                justifyContent: 'center',
                flex: 1,
                backgroundColor: '#78a6f2'
            },
            text: {
                fontFamily: 'latoLight',
                color: 'white',
                fontSize: 24,
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
        return(
            <ScrollView style={styles.container}>
                <Text style={styles.text}>
                    {Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. Hello, like, my name is um, Meghana. }
                </Text>
            </ScrollView>
        )
    }
}