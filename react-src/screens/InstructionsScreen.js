import React, { Component } from 'react'
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native'
import { MaterialIcons } from '@expo/vector-icons';

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
                fontFamily: 'latoLight',
                color: 'white',
                fontSize: 28,
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
            <View style={styles.container}>
                <MaterialIcons
                    name="center-focus-weak"
                    size={50}
                    color={'#fff9'}
                />
                <Text style={styles.text}>Center yourself in the camera.</Text>
                <TouchableOpacity
                    onPress={() => navigate('Recording')}
                    style={styles.button}
                >
                    <Text style={styles.label}>I'M READY!</Text>
                </TouchableOpacity>
            </View>
        )
    }
}