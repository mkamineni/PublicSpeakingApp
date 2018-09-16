import React, { Component } from 'react'
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native'
import { PhoneRotateLandscapeIcon } from 'mdi-react'

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
                fontSize: 28,
            }
        });

        const { navigate } = this.props.navigation;
        return(
            <View style={styles.container}>
                <PhoneRotateLandscapeIcon
                    size={25}
                    color="#0009"
                />
                <Text style={styles.text}>Center yourself in the camera.</Text>
                <TouchableOpacity
                    onPress={() => navigate('Recording')}
                >
                    <Text style={styles.text}>I'M READY!</Text>
                </TouchableOpacity>
            </View>
        )
    }
}