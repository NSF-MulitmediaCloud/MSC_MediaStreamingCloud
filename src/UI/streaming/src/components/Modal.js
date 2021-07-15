import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";


function Modal(props){
return(
    <div className='modal'>
        <p>Are you sure?</p>
        <button className='btn btn--alt' onClick={props.onCancel}>Cancel</button>
        <button className='btn'onClick={props.onConfirm}>Comfirm</button>
        </div>
);
}

export default Modal;