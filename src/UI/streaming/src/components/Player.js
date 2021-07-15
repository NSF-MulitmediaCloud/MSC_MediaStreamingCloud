import React from "react";
import ReactHlsPlayer from "react-hls-player";

function Player(props) {
  const playerRef = props.playerRef;
  //const playerRef = React.createRef();
  //this.playerRef=playerRef;
  function playVideo() {
    playerRef.current.play();
  }

  function pauseVideo() {
    playerRef.current.pause();
  }

  function toggleControls() {
    playerRef.current.controls = !playerRef.current.controls;
  }

  return (
    <ReactHlsPlayer
      playerRef={playerRef}
      src={props.vid}
      hlsConfig={{
        maxLoadingDelay: 4,
        minAutoBitrate: 0,
        lowLatencyMode: true,
      }}
    />
  );
}
export default Player;
