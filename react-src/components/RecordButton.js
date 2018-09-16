import React, { Component } from 'react';
import {
  TouchableOpacity,
  View,
  LayoutAnimation,
  StyleSheet,
} from 'react-native';
import PropTypes from 'prop-types'

export default class RecordingButton extends Component {    
    static propTypes = {
        isRecording: PropTypes.bool,
        onStartPress: PropTypes.func,
        onStopPress: PropTypes.func,
        style: PropTypes.oneOfType([PropTypes.number, PropTypes.object, PropTypes.array]),
    }

    renderRecording(styles) {
        return (
        <TouchableOpacity onPress={this.props.onStopPress}
            style={[styles.buttonContainer, styles.buttonStopContainer, this.props.style]}>
            <View style={styles.buttonStop}></View>
        </TouchableOpacity>
        );
    }

    renderWaiting(styles) {
        return (
        <TouchableOpacity onPress={this.props.onStartPress} style={[styles.buttonContainer, this.props.style]}>
            <View style={styles.circleInside}></View>
        </TouchableOpacity>
        );
    }

    render() {
        const styles = StyleSheet.create({
            buttonContainer: {
                width: 80,
                height: 80,
                borderRadius: 40,
                backgroundColor: '#D91E18',
                alignItems: 'center',
                justifyContent: 'center',
                borderWidth: 5,
                borderColor: 'white',
            },
            circleInside: {
                width: 60,
                height: 60,
                borderRadius: 30,
                backgroundColor: '#D91E18',
            },
            buttonStopContainer: {
                backgroundColor: 'transparent',
            },
            buttonStop: {
                backgroundColor: '#D91E18',
                width: 40,
                height: 40,
                borderRadius: 3,
            },
        });
        if (this.props.isRecording) {
        return this.renderRecording(styles);
        }
        return this.renderWaiting(styles);
    }
}