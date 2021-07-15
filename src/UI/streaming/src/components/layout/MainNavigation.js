import { Link } from "react-router-dom";
import cssclasses from "./MainNavigation.module.css";

function MainNavigation() {
  return (
    <header className={cssclasses.header}>
      <div className={cssclasses.logo}>MSC Streaming Platform (Demo)</div>
      <nav>
        <ul>
          <li>
            <Link to="/streaming">Streaming </Link>
          </li>
          <li>
            <Link to="/setting">Setting </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
