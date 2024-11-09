import { Checkbox } from "../components/ui/checkbox";
import { Button } from "../components/ui/button";
import React from "react";

export default function Home() {

    const [checked, setCheckBox] = React.useState(false);

    const handleChange = (e: boolean) => {
        if (!checked && e) {
            setCheckBox(true);
        } else {
            setCheckBox(false);
        }
    };

    const handleClick = () => {
        console.log(checked);
        if(checked){

        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen min-w-screen bg-black text-gray-800 p-4">
            <div className="w-full bg-white rounded-lg shadow-md p-6 max-h-[100vh] max-w-[40vh]">
                <h1 className="text-3xl font-semibold mb-6 text-center">Home</h1>
                
                <div className="flex items-center space-x-3 mb-4">
                    <Checkbox onClick={() => handleChange(true)}
                        id="terms"
                        className="h-6 w-6 flex-shrink-0 text-blue-500 border-gray-300 rounded focus:ring-blue-500 focus:ring-2 dark:text-blue-500 dark:border-gray-600 dark:focus:ring-blue-500 hover:border-blue-700 hover:bg-blue-100"
                    />
                    <label
                        htmlFor="terms"
                        className="text-lg font-medium text-gray-700 cursor-pointer break-words"
                    >
                        Accept terms and conditions
                    </label>
                </div>
                
                <Button className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-lg transition ease-in-out duration-200 w-full" onClick={() => handleClick()}>
                    Start here
                </Button>
            </div>
        </div>
    );
}
