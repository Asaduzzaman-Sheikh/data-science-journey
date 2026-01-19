import { useState, useEffect } from 'react'
import './App.css'

// Raw data
const rawData = [45, 52, 67, 71, 73, 75, 78, 79, 80, 81, 82, 83, 85, 86, 88, 89, 91, 93, 95, 98];
const bins = [40, 50, 60, 70, 80, 90, 100];
const labels = ['40-49', '50-59', '60-69', '70-79', '80-89', '90-99'];

// Calculate which bin a score belongs to
function getBinIndex(score) {
  for (let i = 0; i < bins.length - 1; i++) {
    if (score >= bins[i] && score < bins[i + 1]) {
      return i;
    }
  }
  return -1;
}

// Steps for the animation
const steps = [
  { id: 1, title: 'Step 1: Raw Data', description: 'Here is our dataset of 20 test scores.' },
  { id: 2, title: 'Step 2: Define Bins', description: 'We divide the range into bins: 40-49, 50-59, 60-69, 70-79, 80-89, 90-99' },
  { id: 3, title: 'Step 3: Assign Scores to Bins', description: 'Each score goes into its corresponding bin...' },
  { id: 4, title: 'Step 4: Count Frequencies', description: 'Count how many scores are in each bin.' },
  { id: 5, title: 'Step 5: Calculate Relative Frequency', description: 'Divide each count by total (20).' },
  { id: 6, title: 'Step 6: Calculate Percentage', description: 'Multiply relative frequency by 100.' },
  { id: 7, title: 'Step 7: Cumulative Frequency', description: 'Running total of frequencies.' },
  { id: 8, title: 'Step 8: Complete!', description: 'The frequency table is complete!' },
];

function App() {
  const [currentStep, setCurrentStep] = useState(1);
  const [assignedScores, setAssignedScores] = useState([]);
  const [animatingScore, setAnimatingScore] = useState(null);
  const [isAutoPlaying, setIsAutoPlaying] = useState(false);
  const [assignmentIndex, setAssignmentIndex] = useState(0);

  // Calculate frequencies based on assigned scores
  const frequencies = labels.map((label, idx) => {
    return assignedScores.filter(s => getBinIndex(s) === idx).length;
  });

  const total = assignedScores.length;

  // Auto-play for step 3 (assigning scores)
  useEffect(() => {
    if (currentStep === 3 && assignmentIndex < rawData.length) {
      const timer = setTimeout(() => {
        setAnimatingScore(rawData[assignmentIndex]);
        setTimeout(() => {
          setAssignedScores(prev => [...prev, rawData[assignmentIndex]]);
          setAnimatingScore(null);
          setAssignmentIndex(prev => prev + 1);
        }, 500);
      }, 300);
      return () => clearTimeout(timer);
    }
  }, [currentStep, assignmentIndex]);

  // Auto-play through steps
  useEffect(() => {
    if (isAutoPlaying && currentStep < 8) {
      const timer = setTimeout(() => {
        if (currentStep === 3 && assignmentIndex < rawData.length) {
          // Wait for all scores to be assigned
          return;
        }
        handleNext();
      }, currentStep === 3 ? 100 : 2000);
      return () => clearTimeout(timer);
    }
  }, [isAutoPlaying, currentStep, assignmentIndex]);

  const handleNext = () => {
    if (currentStep < 8) {
      if (currentStep === 2) {
        // Reset for step 3
        setAssignedScores([]);
        setAssignmentIndex(0);
      }
      setCurrentStep(prev => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentStep > 1) {
      setCurrentStep(prev => prev - 1);
      if (currentStep === 4) {
        setAssignedScores([...rawData]);
        setAssignmentIndex(rawData.length);
      }
    }
  };

  const handleReset = () => {
    setCurrentStep(1);
    setAssignedScores([]);
    setAnimatingScore(null);
    setAssignmentIndex(0);
    setIsAutoPlaying(false);
  };

  return (
    <div className="app">
      <header>
        <h1>📊 Frequency Table: Step-by-Step Animation</h1>
        <p className="subtitle">Learn how pd.cut() creates a frequency table</p>
      </header>

      {/* Step Info */}
      <div className="step-info">
        <h2>{steps[currentStep - 1].title}</h2>
        <p>{steps[currentStep - 1].description}</p>
      </div>

      {/* Progress Bar */}
      <div className="progress-bar">
        {steps.map((step, idx) => (
          <div 
            key={step.id} 
            className={`progress-step ${currentStep > idx ? 'completed' : ''} ${currentStep === idx + 1 ? 'active' : ''}`}
          >
            {idx + 1}
          </div>
        ))}
      </div>

      <div className="main-content">
        {/* Raw Data Section */}
        <div className="section raw-data-section">
          <h3>Raw Data</h3>
          <div className="data-grid">
            {rawData.map((score, idx) => (
              <div 
                key={idx} 
                className={`data-item ${
                  animatingScore === score ? 'animating' : ''
                } ${
                  assignedScores.includes(score) && currentStep >= 3 ? 'assigned' : ''
                }`}
              >
                {score}
              </div>
            ))}
          </div>
          {currentStep >= 1 && (
            <p className="data-info">n = {rawData.length} | Min = {Math.min(...rawData)} | Max = {Math.max(...rawData)}</p>
          )}
        </div>

        {/* Bins Section */}
        {currentStep >= 2 && (
          <div className="section bins-section">
            <h3>Bins</h3>
            <div className="bins-container">
              {labels.map((label, idx) => (
                <div key={idx} className="bin">
                  <div className="bin-label">{label}</div>
                  <div className="bin-box">
                    {currentStep >= 3 && assignedScores
                      .filter(s => getBinIndex(s) === idx)
                      .map((score, sIdx) => (
                        <span key={sIdx} className="bin-score">{score}</span>
                      ))}
                  </div>
                  {currentStep >= 4 && (
                    <div className="bin-count">{frequencies[idx]}</div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Frequency Table */}
        {currentStep >= 4 && (
          <div className="section table-section">
            <h3>Frequency Table</h3>
            <table>
              <thead>
                <tr>
                  <th>Score Range</th>
                  <th>Frequency</th>
                  {currentStep >= 5 && <th>Rel. Freq</th>}
                  {currentStep >= 6 && <th>Percentage</th>}
                  {currentStep >= 7 && <th>Cum. Freq</th>}
                </tr>
              </thead>
              <tbody>
                {labels.map((label, idx) => {
                  const freq = frequencies[idx];
                  const relFreq = total > 0 ? (freq / total).toFixed(2) : '0.00';
                  const pct = total > 0 ? ((freq / total) * 100).toFixed(0) : '0';
                  const cumFreq = frequencies.slice(0, idx + 1).reduce((a, b) => a + b, 0);
                  
                  return (
                    <tr key={idx} className={frequencies[idx] === Math.max(...frequencies) ? 'highlight' : ''}>
                      <td>{label}</td>
                      <td>{freq}</td>
                      {currentStep >= 5 && <td>{relFreq}</td>}
                      {currentStep >= 6 && <td>{pct}%</td>}
                      {currentStep >= 7 && <td>{cumFreq}</td>}
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Controls */}
      <div className="controls">
        <button onClick={handleReset} className="btn reset">🔄 Reset</button>
        <button onClick={handlePrev} disabled={currentStep === 1} className="btn">◀ Previous</button>
        <button 
          onClick={handleNext} 
          disabled={currentStep === 8 || (currentStep === 3 && assignmentIndex < rawData.length)} 
          className="btn primary"
        >
          Next ▶
        </button>
        <button 
          onClick={() => setIsAutoPlaying(!isAutoPlaying)} 
          className={`btn ${isAutoPlaying ? 'active' : ''}`}
        >
          {isAutoPlaying ? '⏸ Pause' : '▶ Auto Play'}
        </button>
      </div>

      {/* Code Reference */}
      {currentStep >= 2 && (
        <div className="code-section">
          <h3>Python Code</h3>
          <pre>
{`import pandas as pd

data = [45, 52, 67, ...]

bins = [40, 50, 60, 70, 80, 90, 100]
labels = ['40-49', '50-59', ...]

df['Bin'] = pd.cut(df['Scores'], bins=bins, labels=labels, right=False)
frequency_table = df['Bin'].value_counts().sort_index()`}
          </pre>
        </div>
      )}
    </div>
  )
}

export default App
