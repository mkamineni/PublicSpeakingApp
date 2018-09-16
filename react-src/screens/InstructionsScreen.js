import React, { Component } from 'react'
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native'

export default class InstructionsScreen extends Component {
    render() {
        const styles = StyleSheet.create({
            container: {
                alignItems: 'center',
                justifyContent: 'center',
                flex: 1,
                backgroundColor: '#78a6f2'
            },
            text: {
                fontFamily: 'latoBold',
                color: 'white',
            }
        });

        const { navigate } = this.props.navigation;
        return(
            <View style={styles.container}>
                <Text style={styles.text}>Hi. This is great!</Text>
                <TouchableOpacity
                    onPress={() => navigate('Recording')}
                >
                    <Text style={styles.text}>I'M READY!</Text>
                </TouchableOpacity>
            </View>
        )
    }
}