import React, { Component } from 'react';
import Expo from 'expo';
import { createStackNavigator } from 'react-navigation';
import StartScreen from './screens/StartScreen';
import InstructionsScreen from './screens/InstructionsScreen';
import RecordingScreen from './screens/RecordingScreen'

const latoBlack = require('./assets/fonts/Lato-Black.ttf');
const latoBlackItalic = require('./assets/fonts/Lato-BlackItalic.ttf');
const latoBold = require('./assets/fonts/Lato-Bold.ttf');
const latoBoldItalic = require('./assets/fonts/Lato-BoldItalic.ttf');
const latoHairline = require('./assets/fonts/Lato-Hairline.ttf');
const latoHairlineItalic = require('./assets/fonts/Lato-HairlineItalic.ttf');
const latoItalic = require('./assets/fonts/Lato-Italic.ttf');
const latoLight = require('./assets/fonts/Lato-Light.ttf');
const latoLightItalic = require('./assets/fonts/Lato-LightItalic.ttf');
const latoRegular = require('./assets/fonts/Lato-Regular.ttf');

export default class App extends Component{
  constructor(props) {
    super(props);
    this.state = {
      fontLoaded: false,
      loading: '',
      msg: '',
      data: []
    };
  }

  componentDidMount() {
    this.loadFonts();
  }

  async loadFonts() {
    // awaits until the font is ready for use
    await Expo.Font.loadAsync({
      latoBlack,
      latoBlackItalic,
      latoBold,
      latoBoldItalic,
      latoHairline,
      latoHairlineItalic,
      latoItalic,
      latoLight,
      latoLightItalic,
      latoRegular
    });
    this.setState({ fontLoaded: true });
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
            msg: 'Video sent',
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
    if (!this.state.fontLoaded){
      return (
        <Expo.AppLoading />
      )
    }
    const App = createStackNavigator({
      Start: { screen: StartScreen },
      Instructions: { screen: InstructionsScreen },
      Recording: { screen: RecordingScreen }
      //Statistics: { screen: StatisticsScreen }
    },
    {
      headerMode: 'none',
      navigationOptions: {
        headerVisible: false,
      }
    });

    return (
      <App />
    );
  }
}

