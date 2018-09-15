import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: '',
      msg: '',
      data: []
    };
  }

  //define more functions later as needed

  sendVideo(page, values) {
    this.setState({ loading: 'sendVideo'}); //check the loading prop in lower components, if its not an empty string display a loading circle
    const body = { form: values};
    fetch(`/api/send`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body),
    })
      .then(res => res.json())
      .then(
        obj => {
          const data = obj.data;
          this.setState({
            loading: '',
            msg: 'Video sent'
            data: [ obj.data ]
          });
        },
        error => {
          this.setState({
            loading: '', 
            msg: 'Error sending video'
          });
          console.error(error);
        }
      );
  }

  handleData = { //contains functions, maybe like retrieveGraph or something
    sendVideo: this.sendVideo
  }

  render() {
    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
      },
    });
    return ( //return a component page that sends in handleData as a prop, as well as the data prop
      <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <Text>Changes you make will automatically reload.</Text>
        <Text>Shake your phone to open the developer menu.</Text>
      </View>
    );
  }
}
