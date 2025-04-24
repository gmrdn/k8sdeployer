
import { ColumnDef } from "@tanstack/react-table"
import { Deployment } from "./model/deployment"


export const columns: ColumnDef<Deployment>[] = [
  {
    accessorKey: "id",
    header: "ID",
  },
  {
    accessorKey: "name",
    header: "Name",
  },
  {
    accessorKey: "image",
    header: "Image",
  },
  {
    accessorKey: "replicas",
    header: "Replicas",
  },
]
