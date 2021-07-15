import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Modal from "./Modal";
import Backdrop from "./Backdrop";

function ControlPane(props) {
  const ControlRef = React.useRef();
  const [modalIsOpen, setModalIsOpen] = React.useState(false);

  function togglePlay() {
    //console.log("clicked");
    //props.thePlayer.toggleControls();
    //props.thePlayer.current.controls = !props.thePlayer.current.controls;
    if (props.thePlayer.current.paused) {
      props.thePlayer.current.play();
    } else {
      props.thePlayer.current.pause();
    }
    //props.thePlayer.playVideo();
  }
  function reload() {
    //console.log("clicked");
    setModalIsOpen(true);
  }
  function closeHandler() {
    setModalIsOpen(false);
  }
  function confirmHandler() {
    console.log("clicked");
    setModalIsOpen(false);
  }
  return (
    <div id="control pane">
      <h2>Control Pane</h2>
      <Button variant="contained" color="primary" onClick={togglePlay}>
        Play/Pause
      </Button>
      <div>
        <TextField></TextField>
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
export default ControlPane;
