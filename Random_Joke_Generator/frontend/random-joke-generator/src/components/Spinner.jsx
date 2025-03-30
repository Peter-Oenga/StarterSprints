import React from "react";

function Spinner() {
    return (
        <div className="flex justify-center items-center">
            <div className="w-8 h-8 border-4 blue-500 border-t-transparent rounded-full animate-spin"></div>
        </div>
    );
}

export default Spinner;