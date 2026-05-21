import { useState } from "react";
import useCart from "./usecart";
import { formatCurrency } from "../../utils/helpers";
import { createOrder } from "./orderservice";
import { initiatePayment } from "./paymentservice";

const Checkout = () => {
  const { cartItems, clearCart } = useCart();

  const [loading, setLoading] = useState(false);

  const totalPrice = cartItems.reduce(
    (total, item) =>
      total + item.price * item.quantity,
    0
  );

  const handleCheckout = async () => {
    try {
      setLoading(true);

      // Create order
      const order = await createOrder({
        items: cartItems,
        total_price: totalPrice,
      });

      // Initiate payment
      await initiatePayment({
        order_id: order.id,
        amount: totalPrice,
      });

      alert("Checkout successful!");

      clearCart();
    } catch (error) {
      console.error(error);

      alert("Checkout failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow">
        <h1 className="text-3xl font-bold mb-6">
          Checkout
        </h1>

        {/* Cart Items */}
        <div className="space-y-4 mb-6">
          {cartItems.map((item) => (
            <div
              key={item.id}
              className="flex justify-between border-b pb-3"
            >
              <div>
                <h2 className="font-semibold">
                  {item.name}
                </h2>

                <p className="text-gray-500">
                  Qty: {item.quantity}
                </p>
              </div>

              <p className="font-bold">
                {formatCurrency(
                  item.price * item.quantity
                )}
              </p>
            </div>
          ))}
        </div>

        {/* Total */}
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">
            Total
          </h2>

          <p className="text-2xl font-bold text-green-700">
            {formatCurrency(totalPrice)}
          </p>
        </div>

        {/* Checkout Button */}
        <button
          onClick={handleCheckout}
          disabled={loading}
          className="w-full bg-green-600 text-white py-3 rounded hover:bg-green-700"
        >
          {loading
            ? "Processing..."
            : "Proceed To Payment"}
        </button>
      </div>
    </div>
  );
};

export default Checkout;