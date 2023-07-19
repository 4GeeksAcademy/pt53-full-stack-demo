import React from "react";

export const Card = ({ img = null, width = "18rem", children }) => {
  const style = {
    width: width,
  };
  return (
    <div className="card mx-auto my-3" style={style}>
      {img ? <img src={img} className="card-img-top" alt="..." /> : ""}
      <div className="card-body">{children}</div>
    </div>
  );
};
