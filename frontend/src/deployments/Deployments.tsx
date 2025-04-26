import { columns } from "./columns"
import { DataTable } from "./DataTable"
import { Deployment } from "./model/deployment"

export type DeploymentsTableProps = {
  deployments: Deployment[]
}

export default function DeploymentsTable(props: DeploymentsTableProps) {
  return (
    <>
      <DataTable
        columns={columns}
        data={props.deployments}
      />
    </>
  )
}
