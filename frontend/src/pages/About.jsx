import './About.css';

function About() {
    return (
        <div className="page-container">
            <h1>About HoopWatch 🏀</h1>
            
            <div className="about-content">
                <section className="about-section">
                    <h2>What is HoopWatch?</h2>
                    <p>
                        HoopWatch is your personalized NBA companion that keeps you connected to the players 
                        and teams you love most. Never miss a game featuring your favorite athletes or franchises. 
                        Our platform aggregates upcoming NBA events and highlights the games that matter most to you, 
                        making it easy to stay on top of the action throughout the season.
                    </p>
                </section>

                <section className="about-section">
                    <h2>How It Works</h2>
                    <p>
                        Simply browse through NBA players and teams, mark your favorites, and we'll automatically 
                        track their upcoming games for you. Your personalized events page will display all scheduled 
                        matchups featuring your selected favorites, complete with game times and matchup details. 
                        Whether you're following a rising star or your hometown team, HoopWatch ensures you're 
                        always in the know.
                    </p>
                </section>

            </div>
        </div>
    );
}

export default About;