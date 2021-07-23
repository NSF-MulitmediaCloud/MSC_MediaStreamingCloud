import React from "react";
//import Player from '../components/Player';
import Player from '../components/Player';
import RequestPane from '../components/RequestPane';
import Context from "../store/user-context";

function StreamingPage(props) {
    //props.children
    const userContext = React.useContext(Context);
    const outerplayerRef=React.useRef();
    userContext.addVideoPlayerO(outerplayerRef);

  return (
    <div>
         
      <h2>Streaming Page</h2>
      <Player vid="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8" ref={outerplayerRef}/>
      <RequestPane vctrl={outerplayerRef}/>
    </div> 
  );
}
export default StreamingPage;
