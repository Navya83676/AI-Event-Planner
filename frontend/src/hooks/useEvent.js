import {
  useContext
} from "react";

import {
  EventContext
} from "../context/EventContext";

const useEvent = () => {

  return useContext(
    EventContext
  );
};

export default useEvent;