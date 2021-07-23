import React, { Component } from "react";
import ReactPlayer from "react-player";
import Button from "@material-ui/core/Button";

// more features example available at https://cookpete.com/react-player/
// and https://github.com/cookpete/react-player/blob/master/src/demo/App.js

class PlayerAlt extends Component {
  state = {
    url: "https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8",
    pip: false,
    playing: false,
    controls: true,
    light: false,
    volume: 0.8,
    muted: false,
    played: 0,
    loaded: 0,
    duration: 0,
    playbackRate: 1.0,
    loop: false,
  };

  load = (url) => {
    this.setState({
      url,
      played: 0,
      loaded: 0,
      pip: false,
    });
  };

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
  };
    */

  handlePlayPause = () => {
    this.setState({ playing: !this.state.playing });
  };
  handleChangeURL = (urlin) => {
    console.log(this.state.url);
    //var urlin ="https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8";
    //setState({url:"https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8"});
    this.load(urlin);
    console.log(this.state.url);
    /*setState({ state.playing: !state.playing }); */
  };
  handleStop = () => {
    this.setState({ url: null, playing: false });
  };

  handleToggleControls = () => {
    this.setState({
      controls: !this.state.controls,
    });
  };

  handleToggleLight = () => {
    this.setState({ light: !this.state.light });
  };

  handleToggleLoop = () => {
    this.setState({ loop: !this.state.loop });
  };

  handleVolumeChange = (e) => {
    this.setState({ volume: parseFloat(e.currentTarget.value) });
  };

  handleToggleMuted = () => {
    this.setState({ muted: !this.state.muted });
  };

  handleSetPlaybackRate = (e) => {
      //console.log(e.currentTarget.value)
    this.setState({ playbackRate: parseFloat(e.currentTarget.value) });
  };

  handleTogglePIP = () => {
    this.setState({ pip: !this.state.pip });
  };

  handlePlay = () => {
    console.log("onPlay");
    this.setState({ playing: true });
  };

  handleEnablePIP = () => {
    console.log("onEnablePIP");
    this.setState({ pip: true });
  };

  handleDisablePIP = () => {
    console.log("onDisablePIP");
    this.setState({ pip: false });
  };

  handlePause = () => {
    console.log("onPause");
    this.setState({ playing: false });
  };

  handleSeekMouseDown = (e) => {
    this.setState({ seeking: true });
  };

  handleSeekChange = (e) => {
    this.setState({ played: parseFloat(e.currentTarget.value) });
  };

  handleSeekMouseUp = (e) => {
    this.setState({ seeking: false });
    this.player.seekTo(parseFloat(e.currentTarget.value));
  };

  handleProgress = (state) => {
    console.log("onProgress", state);
    // We only want to update time slider if we are not currently seeking
    if (!this.state.seeking) {
      this.setState(state);
    }
  };

  handleEnded = () => {
    console.log("onEnded");
    this.setState({ playing: this.state.loop });
  };

  handleDuration = (duration) => {
    console.log("onDuration", duration);
    this.setState({ duration });
  };

  render() {
    const {
      url,
      playing,
      controls,
      light,
      volume,
      muted,
      loop,
      played,
      loaded,
      duration,
      playbackRate,
      pip,
    } = this.state;

    return (
      <div>
        <ReactPlayer
          //ref={playerRef}
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
          onPlay={this.handlePlay}
          onEnablePIP={this.handleEnablePIP}
          onDisablePIP={this.handleDisablePIP}
          onPause={this.handlePause}
          onBuffer={() => console.log("onBuffer")}
          onSeek={(e) => console.log("onSeek", e)}
          onEnded={this.handleEnded}
          onError={(e) => console.log("onError", e)}
          ///
        />
        <h2>Player Control</h2>
        <div>
        <Button
          variant="contained"
          color="primary"
          onClick={this.handlePlayPause}
        >
          {this.playing ? "Pause" : "Play/Pause"}
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={this.handleToggleControls}
        >
          {this.controls ? "Control On" : "Control Off/On"}
        </Button>
        </div>
        <div>
        Speed
        <Button onClick={this.handleSetPlaybackRate} value={0.25} variant="contained"
          color="primary">
          0.25x
        </Button>
        <Button onClick={this.handleSetPlaybackRate} value={0.5} variant="contained"
          color="primary">
          0.5x
        </Button>
        <Button onClick={this.handleSetPlaybackRate} value={1} variant="contained"
          color="primary">
          1x
        </Button>
        <Button onClick={this.handleSetPlaybackRate} value={1.5} variant="contained"
          color="primary">
          1.5x
        </Button>
        <Button onClick={this.handleSetPlaybackRate} value={2} variant="contained"
          color="primary">
          2x
        </Button>
      </div>
      </div>
    );
  }
}
export default PlayerAlt;
