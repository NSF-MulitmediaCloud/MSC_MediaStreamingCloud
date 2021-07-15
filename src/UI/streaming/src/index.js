import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BrowserRouter } from "react-router-dom";

import App from "./App";

//ReactDOM.render(<App />, document.getElementById("root"));

ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById("root")
);

//ReactDOM.render(<MyCustomComponent />, document.getElementById("app"));
//ReactDOM.render(<MyControl />, document.getElementById("control"));
