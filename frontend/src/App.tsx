import { useEffect, useState } from "react";
import { AddDeployment } from "./deployments/AddDeployment"
import DeploymentsTable from "./deployments/Deployments"

 
function App() {
  const [deployments, setDeployments] = useState([])

  const fetchDeployments = async () => {
    const response = await fetch("http://localhost:8000/deployments/");
    const data = await response.json();
    setDeployments(data);
  };

  useEffect(() => {
    fetchDeployments();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-svh gap-4">
      <AddDeployment onCreated={fetchDeployments} />
      <DeploymentsTable deployments={deployments} />
    </div>
  )
}
 
export default App
