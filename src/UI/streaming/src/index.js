import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BrowserRouter } from "react-router-dom";
import {UserContextProvider} from "./store/user-context.js"

import App from "./App";

//ReactDOM.render(<App />, document.getElementById("root"));

ReactDOM.render(
    <UserContextProvider>
  <BrowserRouter>
    <App />
  </BrowserRouter>
  </UserContextProvider>
  ,document.getElementById("root")
);

//ReactDOM.render(<MyCustomComponent />, document.getElementById("app"));
//ReactDOM.render(<MyControl />, document.getElementById("control"));
