window.addEventListener('DOMContentLoaded', function () {
const cashInput = document.getElementById('cash');
    const tenorInput = document.getElementById('tenor');
    const interestInput = document.getElementById('interest');

    const calculateButton = document.getElementById('hitung');
    const resetButton = document.getElementById('reset_hitungan');

    // const resultDiv = document.createElement('div');
    // resultDiv.id = 'simulation_result';
    // document.getElementById('credit_simulation').appendChild(resultDiv);

    const angsuranBulanan = document.getElementById('angsuran_bulanan');
    const totalPembayaran = document.getElementById('total_pembayaran');
    const totalBunga = document.getElementById('total_bunga');

    calculateButton.addEventListener('click', function (event) {
        event.preventDefault();

        const cash = parseFloat(cashInput.value.replace(/,/g, '')) || 0;
        const tenor = parseInt(tenorInput.value) || 0;
        const interest = parseFloat(interestInput.value) || 0;

        if (cash && tenor && interest) {
            const monthlyInterestRate = interest / 100 / 12;
            const monthlyPayment = (cash * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -tenor));
            const totalPayment = monthlyPayment * tenor;
            const totalInterest = totalPayment - cash;

            angsuranBulanan.innerText = `Rp${monthlyPayment.toLocaleString()}`;
            totalPembayaran.innerText = `Rp${totalPayment.toLocaleString()}`;
            totalBunga.innerText = `Rp${totalInterest.toLocaleString()}`;

            // resultDiv.innerHTML = `
            //     <h3>Hasil Simulasi</h3>
            //     <p>Uang Muka: Rp${cash.toLocaleString()}</p>
            //     <p>Tenor: ${tenor} bulan</p>
            //     <p>Bunga: ${interest}% per tahun</p>
            //     <p>Angsuran per bulan: Rp${monthlyPayment.toLocaleString()}</p>
            //     <p>Total Pembayaran: Rp${totalPayment.toLocaleString()}</p>
            //     <p>Total Bunga: Rp${totalInterest.toLocaleString()}</p>
            // `;
        }
    });

    resetButton.addEventListener('click', function () {
        cashInput.value = '';
        tenorInput.value = 12; // Set default tenor to 12 months
        interestInput.value = 5; // Set default interest to 5%
        angsuranBulanan.innerText = '-'
        totalPembayaran.innerText = '-';
        totalBunga.innerText = '-';
    });
});