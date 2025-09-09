const form = document.getElementById('trading-form');
const orderTypeSelect = document.getElementById('order_type');
const priceContainer = document.getElementById('price-container');
const priceInput = document.getElementById('price');
const resultDiv = document.getElementById('result');
const submitBtn = document.getElementById('submit-btn');
const btnText = document.getElementById('btn-text');
const btnSpinner = document.getElementById('btn-spinner');

// --- Event Listeners ---

// Show/hide price input based on order type
orderTypeSelect.addEventListener('change', () => {
    if (orderTypeSelect.value === 'LIMIT') {
        priceContainer.style.display = 'block';
        priceInput.required = true;
    } else {
        priceContainer.style.display = 'none';
        priceInput.required = false;
    }
});

// Handle form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setLoading(true);
    clearResult();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // --- API Call to Backend ---
    try {
        const response = await fetch('http://127.0.0.1:5000/place_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();

        if (response.ok) {
            displaySuccess(result.data);
        } else {
            displayError(result.message || 'An unknown error occurred.');
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        displayError('Could not connect to the backend server. Is it running?');
    } finally {
        setLoading(false);
    }
});

// --- UI Helper Functions ---

function setLoading(isLoading) {
    submitBtn.disabled = isLoading;
    btnText.textContent = isLoading ? 'Placing...' : 'Place Order';
    btnSpinner.style.display = isLoading ? 'block' : 'none';
}

function clearResult() {
    resultDiv.innerHTML = '';
    resultDiv.classList.remove('bg-green-900', 'bg-red-900', 'p-4', 'rounded-b-xl');
}

function displaySuccess(data) {
    resultDiv.classList.add('bg-green-900', 'p-4', 'rounded-b-xl');
    resultDiv.innerHTML = `<h3 class="font-bold text-green-300 mb-2">Order Placed Successfully</h3><pre class="whitespace-pre-wrap break-all text-green-200"><code>${JSON.stringify(data, null, 2)}</code></pre>`;
}

function displayError(message) {
    resultDiv.classList.add('bg-red-900', 'p-4', 'rounded-b-xl');
    resultDiv.innerHTML = `<h3 class="font-bold text-red-300 mb-2">Error</h3><p class="text-red-200">${message}</p>`;
}