import React from "react";

function Editor({ code, setCode }) {
    return (
        <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            rows="10"
            cols="50"
        />
    );
}

export default Editor;
