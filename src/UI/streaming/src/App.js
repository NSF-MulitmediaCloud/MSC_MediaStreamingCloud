import { Route,Switch } from "react-router-dom";
import StreamingPage from "./pages/Streaming";
import SettingPage from "./pages/Setting";
import MainNavigation from "./components/layout/MainNavigation"
function App() {
  return (
    <div>
        <MainNavigation />
        <Switch>
        <Route path='/setting'>
          <SettingPage />
      </Route>
      <Route path='/streaming'>
          <StreamingPage />
      </Route>
      <Route path='/' exact={true}>
          <StreamingPage />
      </Route>
      </Switch>
    </div>
  );
}

export default App;
