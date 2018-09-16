import React, { Component } from 'react'
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native'
import Spinner from 'react-native-loading-spinner-overlay';

export default class LoadingScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            visible: false
    };

    componentDidMount() {
        setInterval(() => {
            this.setState({
            visible: !this.state.visible
            });
        }, 3000);
    }
    render() {
        const { navigate } = this.props.navigation;
        {this.props.loading = "" ? navigate('StatScreen')};
        return(
            <View style={{ flex: 1 }}>
                <Spinner visible={this.state.visible} textContent={"Loading..."} textStyle={{color: '#FFF'}} />
            </View>
        )
    }
} 
