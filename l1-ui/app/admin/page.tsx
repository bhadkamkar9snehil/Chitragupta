import type { Metadata } from "next";
import { Console } from "@/components/console/shell";

export const metadata: Metadata = { title: "Support console · XBatch Helpdesk" };

export default function AdminPage() {
  return <Console />;
}
