import React from "react";
import ReactHlsPlayer from "react-hls-player";
import Context from "../store/user-context";

function Player(props) {
  const userContext = React.useContext(Context);
  const playerRef = React.useRef();
  userContext.addVideoPlayer(playerRef.current);
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
