import { useEffect, useState } from "react";
import { getOrders } from "../buyer/orderservice";
import { formatCurrency, formatDate } from "../../utils/helpers";

const FarmerOrders = () => {
  const [orders, setOrders] = useState([]);

  const fetchOrders = async () => {
    try {
      const data = await getOrders();
      setOrders(data);
    } catch (error) {
      console.error("Failed to fetch orders:", error);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-green-700">
          Farmer Orders
        </h1>

        <p className="text-gray-600 mt-2">
          Manage incoming customer orders
        </p>
      </div>

      {/* Orders Table */}
      <div className="bg-white shadow rounded-lg overflow-x-auto">
        <table className="w-full border-collapse">
          <thead className="bg-green-600 text-white">
            <tr>
              <th className="text-left p-4">Order ID</th>
              <th className="text-left p-4">Customer</th>
              <th className="text-left p-4">Product</th>
              <th className="text-left p-4">Quantity</th>
              <th className="text-left p-4">Total</th>
              <th className="text-left p-4">Status</th>
              <th className="text-left p-4">Date</th>
            </tr>
          </thead>

          <tbody>
            {orders.length > 0 ? (
              orders.map((order) => (
                <tr
                  key={order.id}
                  className="border-b hover:bg-gray-50"
                >
                  <td className="p-4">
                    #{order.id}
                  </td>

                  <td className="p-4">
                    {order.customer_name}
                  </td>

                  <td className="p-4">
                    {order.product_name}
                  </td>

                  <td className="p-4">
                    {order.quantity}
                  </td>

                  <td className="p-4">
                    {formatCurrency(order.total_price)}
                  </td>

                  <td className="p-4">
                    <span
                      className={`px-3 py-1 rounded-full text-sm text-white ${
                        order.status === "delivered"
                          ? "bg-green-600"
                          : order.status === "pending"
                          ? "bg-yellow-500"
                          : "bg-red-500"
                      }`}
                    >
                      {order.status}
                    </span>
                  </td>

                  <td className="p-4">
                    {formatDate(order.created_at)}
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td
                  colSpan="7"
                  className="text-center p-6 text-gray-500"
                >
                  No orders available
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default FarmerOrders;