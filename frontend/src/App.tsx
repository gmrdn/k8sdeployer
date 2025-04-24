import { AddDeployment } from "./deployments/AddDeployment"
import DeploymentsTable from "./deployments/Deployments"

 
function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-svh gap-4">
      <AddDeployment />
      <DeploymentsTable />
    </div>
  )
}
 
export default App
