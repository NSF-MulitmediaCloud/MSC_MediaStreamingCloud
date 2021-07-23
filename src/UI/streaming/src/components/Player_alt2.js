import React from "react";
import ReactPlayer from "react-player";
import Context from "../store/user-context";

function PlayerAlt(props) {
  const userContext = React.useContext(Context);
  const playerRef = React.useRef();
  const outerplayerRef=React.useRef();

  const [url,setUrl]=React.useState("https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8");
  const [pip,setPip]=React.useState(false);
  const [playing,setPlaying]=React.useState(false);
  const [controls,setControls]=React.useState(false);
  const [light,setLight]=React.useState(false);
  const [volume,setVolume]=React.useState(0.8);
  const [muted,setMuted]=React.useState(false);
  const [played,setPlayed]=React.useState(0);
  const [loaded,setLoaded]=React.useState(0);
  const [duration,setCuration]=React.useState(0);
  const [loop,setLoop]=React.useState(false);
  const [playbackRate,setPlaybackRate]=React.useState(1.0);

  userContext.addVideoPlayerO(outerplayerRef);
  userContext.addVideoPlayer(playerRef.current);
  const load = urlin => {
      console.log("on load url in="+urlin);
      setPlaying(false);
      setPlayed(0);
      setLoaded(0);
      setPip(false);
      setUrl(urlin);

      /*
    setState((prevState) => { return {
      url: urlin,
      played: 0,
      loaded: 0,
      playing: false,
      pip: false,
      ...prevState
    }}
    );
    */
  };
  const handlePlayPause = () => {

    console.log("playing " + url + " " + playing);
    setPlaying(!playing);
    console.log(playing);
    /*setState({ state.playing: !state.playing }); */
  };
  const handleChangeURL = () => {
    console.log(url);
    var urlin =
      "https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8";
    //setState({url:"https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8"});
    load(urlin);
    console.log(url);
    /*setState({ state.playing: !state.playing }); */
  };
  const handlePlay = () => {
    console.log("onPlay");
    setPlaying(true);
  };
  const handleEnablePIP = () => {
    console.log("onEnablePIP");
    setPip(true);
  };

  const handleDisablePIP = () => {
    console.log("onDisablePIP");
    setPip(false);
  };
  const handlePause = () => {
    console.log("onPause");
    setPlaying(false);
  };
  const handleEnded = () => {
    console.log("onEnded");
    setPlaying(loop);
  };

  return (
    <div ref={outerplayerRef}>
      <ReactPlayer
        ref={playerRef}
        //playerRef={playerRef}
        //url={props.vid}
        url={url}
        ///
        width="100%"
        height="100%"
        pip={pip}
        playing={playing}
        controls={controls}
        light={light}
        loop={loop}
        playbackRate={playbackRate}
        volume={volume}
        muted={muted}
        onReady={() => console.log("onReady")}
        onStart={() => console.log("onStart")}
        onPlay={handlePlay}
        onEnablePIP={handleEnablePIP}
        onDisablePIP={handleDisablePIP}
        onPause={handlePause}
        onBuffer={() => console.log("onBuffer")}
        onSeek={(e) => console.log("onSeek", e)}
        onEnded={handleEnded}
        onError={(e) => console.log("onError", e)}
        ///
      />
      <button onClick={handlePlayPause}>{playing ? "Pause" : "Play"}</button>
      <button onClick={handleChangeURL}>New URL</button>
    </div>
  );
}
export default PlayerAlt;
