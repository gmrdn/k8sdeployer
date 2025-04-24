
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from "react"
 
export function AddDeployment() {
  const [name, setName] = useState("my-nginx-deployment")
  const [image, setImage] = useState("nginx:1.14.2")
  const [open, setOpen] = useState(false)

  const handleCreate = () => {
    const deployment = {
      name,
      image,
    }

    fetch("http://localhost:8000/deployment/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(deployment),
    })
      .then((res) => res.json())
      .then(() => {
        setOpen(false)
      })


  }
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="outline">Add Deployment</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Add Deployment</DialogTitle>
          <DialogDescription>
            Create a new Deployment. Click save when you're done.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="name" className="text-right">
              Name
            </Label>
            <Input id="name" value={name} className="col-span-3" onChange={(e) => setName(e.target.value)} />
          </div>
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="username" className="text-right">
              Image
            </Label>
            <Input id="username" value={image} className="col-span-3" onChange={(e) => setImage(e.target.value)} />
          </div>
        </div>
        <DialogFooter>
          <Button type="submit" onClick={handleCreate}>Save changes</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
