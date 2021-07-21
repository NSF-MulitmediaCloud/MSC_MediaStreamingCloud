import React from "react";
import Player from '../components/Player';
import ControlPane from '../components/ControlPane';

function StreamingPage(props) {
    //props.children
  return (
    <div>
        
      <p>Streaming Page</p>
      <Player vid="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8"/>
      <ControlPane/>
    </div>
  );
}
export default StreamingPage;
