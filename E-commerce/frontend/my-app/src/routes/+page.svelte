<script>
     import { onMount } from 'svelte';
    import '@fortawesome/fontawesome-free/css/all.min.css';

    import Chart from 'chart.js/auto';
  
  let chart1, chart2;
  
  // Example data for charts
  let businessTrendData = [3000, 4500, 5000, 6500, 8000, 10000]; // Business trend data
  let locationTrendData = [4000, 6000, 8000, 5000, 7000]; // Location data
  
  // Example labels
  let timeLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']; // Monthly labels for business trend
  let locationLabels = ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5']; // Location labels
  
  // Function to initialize the charts after the DOM is loaded
  const createCharts = () => {
    // Business trend chart (Futuristic Line Chart)
    const ctx1 = document.getElementById('chart1').getContext('2d');
    chart1 = new Chart(ctx1, {
      type: 'line',
      data: {
        labels: timeLabels,
        datasets: [{
          label: 'Business Trend',
          data: businessTrendData,
          backgroundColor: 'rgba(0, 255, 255, 0.1)', // Light cyan fill
          borderColor: '#00FFFF', // Cyan border
          borderWidth: 2,
          pointRadius: 5,
          pointBackgroundColor: '#ff7e00' // Orange points
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        plugins: {
          legend: {
            display: true,
            labels: {
              color: '#00FFFF'
            }
          }
        },
        elements: {
          line: {
            tension: 0.4 // Smooth curves
          }
        }
      }
    });

    // Location performance chart
    const ctx2 = document.getElementById('chart2').getContext('2d');
    chart2 = new Chart(ctx2, {
      type: 'line',
      data: {
        labels: locationLabels,
        datasets: [{
          label: 'Location Performance',
          data: locationTrendData,
          backgroundColor: 'rgba(255, 69, 0, 0.1)', // Light red fill
          borderColor: '#FF4500', // Red border
          borderWidth: 2,
          pointRadius: 5,
          pointBackgroundColor: '#ff4500' // Red points
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        plugins: {
          legend: {
            display: true,
            labels: {
              color: '#FF4500'
            }
          }
        },
        elements: {
          line: {
            tension: 0.4 // Smooth curves
          }
        }
      }
    });
  };

  // Trigger chart creation when the component mounts
  onMount(() => {
    createCharts();
  });


  
    // State variables for toggling navigation and progress bars in mobile view
    let showNav = false;
    let showProgressBars = true;
  
    // Example progress data in KES
    let progressData = [
      { label: 'Location 1', value: 4000 },
      { label: 'Location 2', value: 6000 },
      { label: 'Location 3', value: 8000 },
      { label: 'Location 4', value: 5000 },
      { label: 'Location 5', value: 7000 }
    ];
  
    // Calculate the total points in KES
    let totalPoints = progressData.reduce((sum, progress) => sum + progress.value, 0);
  
    let currentPoints = 4500; // Example value
    let progressPercentage = (currentPoints / totalPoints) * 100;
  
    // Ensure progress percentage is between 0 and 100
    progressPercentage = Math.min(Math.max(progressPercentage, 0), 100);
    
    // Simulate the current points, for example purposes
    currentPoints = totalPoints;
  
    // Generate the gradient background for the circular progress bar
    let gradientBackground = `conic-gradient(
      #ff7e00 0%,
      #ff7e00 ${progressPercentage}%,
      #ff4500 ${progressPercentage}%,
      #ff4500 ${progressPercentage + 10}%, /* Adjust to show segment */
      #dc143c ${progressPercentage + 10}%,
      #dc143c 100%
    )`;
  </script>
  
  <style>
    /* General page layout */
    .container {
      display: flex;
      height: 100vh;
      overflow: hidden;
    }
  
    .nav {
      background-color: #2b2d42;
      color: white;
      width: 20%;
      min-width: 200px;
      padding: 20px;
      transition: transform 0.3s ease;
    }
  
    .nav ul {
      list-style-type: none;
      padding: 0;
    }
  
    .nav ul li {
      margin: 20px 0;
      display: flex;
      align-items: center;
    }
  
    .nav ul li a {
      color: white;
      text-decoration: none;
      display: flex;
      align-items: center;
    }
  
    .nav ul li a .fab-icon {
      background-color: #edf2f4;
      color: #2b2d42;
      border-radius: 50%;
      padding: 10px;
      margin-right: 10px;
      font-size: 1.2rem;
    }
  
    .map-container {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      background-color: #edf2f4;
    }
  
    .map {
      flex: 1;
      background-color: #fff;
      border-bottom: 1px solid #ccc;
      overflow: hidden;
    }
  
    .map iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  
    .graph {
    height: 400px;
    background-color: #1c1e26;
    color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .graph h2 {
    color: #00FFFF; /* Cyan futuristic font */
  }

  canvas {
    margin: 20px 0;
    max-width: 100%;
  }
  
    /* Container for progress bars */
    .progress-bars-container {
      width: 20%;
      background-color: #8d99ae;
      padding: 20px;
      overflow-y: auto;
      border-left: 1px solid #ccc;
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  
    
  
    .progress-bars {
      text-align: center;
      margin: 60px 0 20px;
      width: 100%;
    }
  
    .progress-bars .progress {
      margin: 20px 0;
    }
  
    .progress-bars .progress-bar {
      height: 20px;
      background-color: #ddd;
      border-radius: 5px;
      overflow: hidden;
      position: relative;
    }
  
    .progress-bars .progress-bar div {
      height: 100%;
      background: linear-gradient(to right, #ff7e00, #ff4500, #dc143c);
      color: white;
      text-align: center;
      line-height: 20px;
      position: absolute;
      left: 0;
      top: 0;
    }
  
    .progress-bars .progress-bar.circle {
      position: relative;
      display: inline-block;
      width: 150px;
      height: 150px;
      border-radius: 50%;
      margin: 20px 0;
      background: var(--progress-gradient);
    }
  
    .progress-bars .progress-bar.circle .progress-bar-fill {
      position: absolute;
      border-radius: 50%;
      width: 100%;
      height: 100%;
      clip: rect(0, 150px, 150px, 75px);
      background: transparent;
    }
  
    .progress-bars .progress-bar.circle .progress-bar-fill::after {
      content: "Target: KES 10000\nCurrent: KES {currentPoints}";
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: #333;
      text-align: center;
      font-size: 14px;
      line-height: 1.5;
    }
  
    /* Mobile view */
    @media (max-width: 768px) {
      .container {
        flex-direction: column;
      }
  
      .nav {
        display: none;
        width: 100%;
        transform: translateX(-100%);
      }
  
      .nav.show {
        display: block;
        transform: translateX(0);
      }
  
      .hamburger {
        display: block;
        background-color: #2b2d42;
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
        width: 100%;
      }
  
      .progress-bars-container {
        display: none;
        width: 100%;
      }
  
      .progress-bars-container.show {
        display: block;
      }
  
      .show-progress-bars-btn {
        display: block;
        background-color: #2b2d42;
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
        width: 100%;
      }
    }
  
    /* Non-mobile view (desktop/tablet) */
    .hamburger, .show-progress-bars-btn {
      display: none;
    }
  </style>
  
  <!-- Container for the three-column layout -->
  <div class="container">
    <!-- Navigation Section -->
    <div class="nav {showNav ? 'show' : ''}">
      <button class="hamburger" on:click={() => showNav = !showNav}>☰ Menu</button>
      <h1>ROckBizz</h1>
      <ul>
        <li>
          <a href="#">
            <i class="fa-solid fa-house fab-icon"></i> <!-- Home Icon -->
            Home
          </a>
        </li>
        <li>
          <a href="#">
            <i class="fa-solid fa-bell fab-icon"></i> <!-- Notification Icon -->
            Notification
          </a>
        </li>
        <li>
          <a href="#">
            <i class="fa-solid fa-phone-volume fab-icon"></i> <!-- Contact Icon -->
            Contact
          </a>
        </li>
        <li>
          <a href="#">
            <i class="fa-duotone fa-solid fa-gear fab-icon"></i> <!-- Settings Icon -->
            Settings
          </a>
        </li>
        <li>
          <a href="#">
            <i class="fa-sharp fa-solid fa-circle-info fab-icon"></i> <!-- Help Icon -->
            Help
          </a>
        </li>
      </ul>
    </div>
  
    <!-- Map and Graph Section -->
    <div class="map-container">
      <!-- Map Section -->
      <div class="map">
        <iframe src="/map.html" title="Map"></iframe>
      </div>
  
      <!-- Graph Section -->
    <div class="graph">
  <h2>Performance Analyzer</h2>
  
  <!-- Business Trend Chart -->
  <canvas id="chart1" width="400" height="200"></canvas>
  
  <!-- Location Performance Chart -->
  <canvas id="chart2" width="400" height="200"></canvas>
  </div>

    </div>
  
    <!-- Progress Bars Section -->
    <div class="progress-bars-container">
      <h4 style="font-size: larger;"> Location Analyzer</h4>
      <button class="show-progress-bars-btn" on:click={() => showProgressBars = !showProgressBars}>
        {showProgressBars ? 'Hide Progress Bars' : 'Show Progress Bars'}
      </button>
      {#if showProgressBars}
        <!-- Circular Progress Bar -->
        <div class="progress-bars">
          <div class="progress-bar circle" style="--progress-gradient: {gradientBackground};">
            <div class="progress-bar-fill"></div>
          </div>
  
          <!-- Straight Progress Bars -->
          {#each progressData as progress}
            <div class="progress">
              <div>{progress.label}</div>
              <div class="progress-bar">
                <div style="width: {progress.value / totalPoints * 100}%">
                  KES {progress.value}
                </div>
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </div>
  </div>
  