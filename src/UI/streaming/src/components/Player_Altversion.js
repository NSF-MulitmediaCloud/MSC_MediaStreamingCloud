import React from "react";
import ReactHlsPlayer from "react-hls-player";
import Context from "../store/user-context";

function Player(props) {
  const outerplayerRef=React.useRef();
  const userContext = React.useContext(Context);
  const playerRef = React.useRef();
  userContext.addVideoPlayer(playerRef.current);
  userContext.addVideoPlayerO(outerplayerRef);

  return (
    <ReactHlsPlayer
      ref={outerplayerRef}
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
