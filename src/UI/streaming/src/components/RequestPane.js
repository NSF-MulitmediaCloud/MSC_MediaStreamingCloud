import process from 'process';
import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormLabel from "@material-ui/core/FormLabel";
import NativeSelect from "@material-ui/core/NativeSelect";
import InputLabel from "@material-ui/core/InputLabel";
import FormHelperText from "@material-ui/core/FormHelperText";

import Modal from "./Modal";
import Backdrop from "./Backdrop";
import Context from "../store/user-context";

function RequestPane(props) {
    //console.log(process.env);
  const Webportal_addr = process.env.REACT_APP_REQURL || 'reqforward'; //'http://adc.core:60008';

  const ControlRef = React.useRef();
  var vidsrc = React.useRef(); 
  //const [vidsrc, setvidsrc] = React.useState();

  
  const resXref = React.useRef();
  const resYref = React.useRef();
  const frref = React.useRef();

  const [modalIsOpen, setModalIsOpen] = React.useState(false);
  const userContext = React.useContext(Context);
  const [color, setcolor] = React.useState("normal");
  const [codec, setCodec] = React.useState("h264");
  const [audio, setAudio] = React.useState(" -acodec copy");
  const [rotate, setRotate] = React.useState("");
  const [vidNum, setvidNum] = React.useState(1);
  var vidoptions = []; //eventually, will collect from server
  for (var i = 1; i <= 100; i++) {
    var anoption = {};
    anoption["value"] = i;
    anoption["label"] = i + "";
    vidoptions.push(anoption);
  }
  function submitHandler(event) {
    event.preventDefault();
    //var ffoptions="-profile:v baseline -copyts "+ $("#framerate").val()+" "+$("#resolution").val()+$("#color").val()+$("#rotate").val()+" "+$("#vcodec").val()+" "+$("#acodec").val()
    var ffoptions =
      "-profile:v baseline -copyts " +
      " -vf scale=" +
      resXref.current.value +
      "x" +
      resYref.current.value;
    if (color !== "normal") {
      ffoptions += color;
    }
    ffoptions += rotate;
    ffoptions += " -r " + frref.current.value + " -c:v " + codec + audio;
    //console.log("Test Submit to"+url);
    //console.log("Message:" + ffoptions);
    var data={option: ffoptions, vidnum: vidNum}
    fetch(Webportal_addr,{
      method: 'POST', // or 'PUT'
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      if(data['returnedurl']){
        console.log(data['returnedurl'])
        vidsrc.value=(data['returnedurl']);
        console.log(vidsrc.value);
      }
    })
    .catch((error) => {
      console.error('Error:', error);


    });
    
  }
  const handleChangeVidNum = (event) => {
    setvidNum(event.target.value);
  };
  const handleChangeRotate = (event) => {
    setRotate(event.target.value);
  };
  // const handleChangeSource = (event) => {
  //   setvidsrc(event.target.value);
  // };
  
  const handleChangeAudio = (event) => {
    setAudio(event.target.value);
  };
  const handleChangeColor = (event) => {
    setcolor(event.target.value);
  };
  const handleChangeCodec = (event) => {
    setCodec(event.target.value);
  };
  function loadandPlayVideo(vsource){
    console.log("reload from: "+vsource);
    //userContext.videoplayerO.setAttribute('src', vsource);
    props.vctrl.current.handleChangeURL(vsource);
  }

  function reload() {
    //console.log("clicked");
    setModalIsOpen(true);
  }
  function closeHandler() {
    setModalIsOpen(false);
  }
  function confirmHandler() {
    loadandPlayVideo(vidsrc.value);
    console.log("reloaded " + vidsrc.value);
    setModalIsOpen(false);
  }
  return (
    <div id="request pane">
      <h2>Request Pane</h2>
      <div>
        <form onSubmit={submitHandler}>
          <FormControl>
            <InputLabel htmlFor="video selector">Video Number</InputLabel>
            <NativeSelect
              value={vidNum}
              onChange={handleChangeVidNum}
              inputProps={0}
            >
              {vidoptions.map(({ value, label }, index) => (
                <option value={value}>{label}</option>
              ))}
            </NativeSelect>
            <FormHelperText>Select Video number from a list</FormHelperText>
          </FormControl>
          <TextField
            label="Resolution X"
            variant="filled"
            defaultValue="1920"
            inputRef={resXref}
          />
          <TextField
            label="Resolution Y"
            variant="filled"
            defaultValue="1080"
            inputRef={resYref}
          />
          <TextField
            label="Framerate (FPS)"
            variant="filled"
            defaultValue="30"
            inputRef={frref}
          />
          <div></div> {/* line break */}

          <FormControl component="fieldset">
            <FormLabel component="legend">Color Profile</FormLabel>
            <RadioGroup
              aria-label="Color"
              name="vidcolor1"
              value={color}
              onChange={handleChangeColor}
            >
              <FormControlLabel
                value="normal"
                control={<Radio />}
                label="Normal"
              />
              <FormControlLabel
                value=",hue=s=0"
                control={<Radio />}
                label="B & W"
              />
              {/* <FormControlLabel value="normal" control={<Radio />} label="Sepia" /> */}
              <FormControlLabel
                value="other"
                disabled
                control={<Radio />}
                label="Sepia"
              />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset">
            <FormLabel component="legend">Audio</FormLabel>
            <RadioGroup
              aria-label="Audio"
              name="audiogroup"
              value={audio}
              onChange={handleChangeAudio}
            >
              <FormControlLabel
                value=" -acodec copy"
                control={<Radio />}
                label="On"
              />
              <FormControlLabel value=" -an" control={<Radio />} label="Mute" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset">
            <FormLabel component="legend">Rotate</FormLabel>
            <RadioGroup
              aria-label="Rotate"
              name="rotategroup"
              value={rotate}
              onChange={handleChangeRotate}
            >
              <FormControlLabel
                value=""
                control={<Radio />}
                label="Normal Orientation"
              />
              <FormControlLabel
                value=",transpose=2,transpose=2"
                control={<Radio />}
                label="UpsideDown"
              />
            </RadioGroup>
          </FormControl>

          <FormControl component="fieldset">
            <FormLabel component="legend">Codec</FormLabel>
            <RadioGroup
              aria-label="Codec"
              name="codecgroup1"
              value={codec}
              onChange={handleChangeCodec}
            >
              <FormControlLabel
                value="h264"
                control={<Radio />}
                label="H.264"
              />
              <FormControlLabel
                value="h265"
                control={<Radio />}
                label="H.265"
              />
              <FormControlLabel value="vp9" control={<Radio />} label="VP9" />
            </RadioGroup>
          </FormControl>
          <div></div> {/* line break */}

          <Button variant="contained" color="primary" type="submit">
            Request This version
          </Button>
        </form>
      </div>
      <div>
      <TextField
            label="Video Source"
            variant="filled"
            defaultValue="https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8"
            inputRef={(input) => vidsrc = input}
          />
        <Button variant="contained" color="secondary" onClick={reload}>
          Reload
        </Button>
      </div>
      {modalIsOpen && <Backdrop onCancel={closeHandler} />}
      {modalIsOpen && (
        <Modal onCancel={closeHandler} onConfirm={confirmHandler} />
      )}
    </div>
  );
}
//export default MyCustomComponent;
export default RequestPane;
