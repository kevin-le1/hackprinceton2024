import { useNavigate } from "react-router-dom";
import { Button } from "../components/ui/button";


export default function Dash() {

    const navigate = useNavigate();
    const back = () => {
        navigate('/input');
    };
      

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>    
            <Button
                className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-lg transition ease-in-out duration-200"
                onClick={() => back()}>
                Back
            </Button>
        </div>
    );
}
