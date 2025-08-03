import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

const mockData = [
  { time: "08:00", usage: 1.2 },
  { time: "09:00", usage: 1.5 },
  { time: "10:00", usage: 1.3 },
  { time: "11:00", usage: 1.8 },
  { time: "12:00", usage: 2.0 },
  { time: "13:00", usage: 1.6 },
];

export default function ElectricityDashboard() {
  const [currentUsage, setCurrentUsage] = useState(0);
  const [costEstimate, setCostEstimate] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      const usage = (Math.random() * 2 + 1).toFixed(2);
      setCurrentUsage(usage);
      setCostEstimate((usage * 0.15).toFixed(2)); // Assume $0.15/kWh
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6">Electricity Monitoring Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <Card>
          <CardContent>
            <p className="text-sm text-gray-500">Current Usage</p>
            <h2 className="text-2xl font-semibold">{currentUsage} kW</h2>
          </CardContent>
        </Card>
        <Card>
          <CardContent>
            <p className="text-sm text-gray-500">Estimated Cost (per hour)</p>
            <h2 className="text-2xl font-semibold">${costEstimate}</h2>
          </CardContent>
        </Card>
        <Card>
          <CardContent>
            <p className="text-sm text-gray-500">Peak Usage</p>
            <h2 className="text-2xl font-semibold">2.0 kW</h2>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardContent>
          <h3 className="text-xl font-semibold mb-4">Usage Over Time</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={mockData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis unit="kW" />
              <Tooltip />
              <Line type="monotone" dataKey="usage" stroke="#4f46e5" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
}
