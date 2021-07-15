import React from "react";
import Player from '../components/Player';
import ControlPane from '../components/ControlPane';

function StreamingPage(props) {
    const playerRef = React.createRef();

    //props.children
  return (
    <div>
        
      <p>Streaming Page</p>
      <Player vid="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8" playerRef={playerRef}/>
      <ControlPane thePlayer={playerRef} />
    </div>
  );
}
export default StreamingPage;
