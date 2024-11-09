import '../App.css'
import {Checkbox} from "../components/ui/checkbox"
import {Button} from "../components/ui/button"

export default function Home () {

  return (
    <>
        <div>Home</div>
        
        <div className="flex space-x-3">


        <Checkbox
        id="terms"
        className="h-5 w-5 text-blue-500 border-gray-300 rounded focus:ring-blue-500 focus:ring-2 dark:text-blue-500 dark:border-gray-600 dark:focus:ring-blue-500 hover:border-blue-700 hover:bg-blue-100"
        />
        <label
        htmlFor="terms"
        className="text-sm font-medium text-white dark:text-gray-300 cursor-pointer"
        >
        Accept terms and conditions
        </label>
        <Button>Start here</Button>
        </div>
        </>
  )
}