import React from "react";

const SettingContext = React.createContext({
  myfunctions: [],
  fncount: 0,
  Vidplayer:0,
  addFunction: (userFunction) => {},
  removeFunction: (FunctionID) => {},
  functionIsEmployed: (FunctionID) =>{},
  addVideoPlayer: (videoPlayer) => {},
  addVideoPlayerO: (videoPlayerO) => {}

});
export function UserContextProvider(props) {
  const [userFunctions, setUserFunctions] = React.useState([]);
  const [videoPlayers,setVideoPlayers] = React.useState(0);
  const [videoPlayersO,setVideoPlayersO] = React.useState(0);

  function addVideoPlayerHandler(videoPlayer){
    //return Vidplayer=videoPlayer;
    setVideoPlayers((prevvideoPlayer) => {
        return prevvideoPlayer=(videoPlayer);
    });
  }
  function addVideoPlayerOHandler(videoPlayersO){
    //return Vidplayer=videoPlayer;
    setVideoPlayersO((prevvideoPlayerO) => {
        return prevvideoPlayerO=(videoPlayersO);
    });
  }
  function addFunctionHandler(userFunction){
    setUserFunctions((prevmyfunctions) => {
        return prevmyfunctions.concat(userFunction);
    });
  }
  function removeFunctionHandler(FunctionID){
    setUserFunctions((prevmyfunctions) => {
        return prevmyfunctions.filter(myfunctions => myfunctions.id !== FunctionID);
    });
  }
  function functionIsEmployedHandler(FunctionID){
    setUserFunctions((prevmyfunctions) => {
        return prevmyfunctions.some(myfunctions => myfunctions.id === FunctionID)
    });
  }

  const context = {
    videoplayer: videoPlayers,
    videoplayerO: videoPlayersO,
    myfunctions: userFunctions,
    fncount: userFunctions.length,
    addFunction: addFunctionHandler,
    removeFunction: removeFunctionHandler,
    functionIsEmployed: functionIsEmployedHandler,
    addVideoPlayer: addVideoPlayerHandler,
    addVideoPlayerO: addVideoPlayerOHandler
};

  return (
    <SettingContext.Provider value={context}>
      {props.children}
    </SettingContext.Provider>
  );
}
export default SettingContext;