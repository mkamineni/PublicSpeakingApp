import React, { Component } from 'react'
import { TouchableOpacity, View, StyleSheet, Text } from 'react-native'

export default class StartScreen extends Component {
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
            }
        });

        const { navigate } = this.props.navigation;
        return (
            <View style={styles.container}>
                <TouchableOpacity
                    onPress={() => navigate('Instructions')}
                >
                    <Text style={styles.text}>START RECORDING</Text>
                </TouchableOpacity>
            </View>
        )
    }
}