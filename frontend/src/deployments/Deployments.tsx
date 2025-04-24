import { useState, useEffect } from "react"
import { columns } from "./columns"
import { DataTable } from "./DataTable"

export default function DeploymentsTable() {
  const [deployments, setDeployments] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/deployments/")
      .then((res) => res.json())
      .then(setDeployments)
  }, [])

  return (
    <>
      <DataTable
        columns={columns}
        data={deployments}
      />
    </>
  )
}
