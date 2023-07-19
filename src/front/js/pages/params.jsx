import React, { useContext } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const Params = () => {
  const { message } = useParams();

  const { store, actions } = useContext(Context);

  // RRD docs: https://reactrouter.com/en/main

  return (
    <>
      <h1>{message}</h1>
      <p onClick={actions.changeMessage}>{store.message}</p>
      <p>{store.message}</p>
      <p>{store.message}</p>
      <p>{store.message}</p>
      <p>{store.message}</p>
      <p>{store.message}</p>
      <p>{store.message}</p>
      <p>{store.message}</p>
    </>
  );
};
