from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['MAIL_SERVER'] = 'smtp.mail.me.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

articles = {
    'intellectual-property': {
        'title': 'Intellectual Property in Italy and the EU',
        'topic': 'Law & Tech',
        'content': '''
<p>Intellectual property law protects creative and mental works, including innovations, artworks, designs, and symbols. Italy, with its rich heritage of art, culture, and innovation, has significantly shaped intellectual property regulations. This field of law safeguards creators rights through three main tools: copyright, trademarks, and patents. It functions as an umbrella term encompassing both copyright and industrial property protection.</p>

<h2>The Early Foundations</h2>
<p>Italy's mark in intellectual property started in 1474 with the Venetian Patent Act, often seen as the first modern patent law. This rule gave makers sole rights to their work for ten years, keeping safe and pushing new ideas. For example a 15th-century maker of a big machine could get one-of-a-kind use, stopping others from copying it.</p>
<p>In the time of the Renaissance, the growth of arts, science and invention showed a bigger need for protecting ideas. Makers, from painters to builders, wanted praise and uniqueness making way for today's idea rules.</p>

<h2>The 19th Century: Unification and Industrial Growth</h2>
<p>The Unification of Italy with its regional spheres in 1861 resulted in essential changes in intellectual property law. The 1859 Sardinian Law on Industrial Property constituted the base of the national Italian patent system. This unified framework not only allowed Italian industry to develop but protected the industries of other countries from competition. In the meantime, the Industrial Revolution was progressing and a new economy developed, with new machines, tools, and processes, all of which could not be built using traditional methods of artisanal work-production, and under which protection was necessary.</p>
<p>The Italian Civil Code 1865 (Codice Civile del Regno d'Italia) contained minimal copyright provisions, delegating these matters to specialized statutes. The Code was influenced by French Napoleonic tradition, focusing on general private law while leaving intellectual property specifics to specialized legislation, primarily the Legge sul diritto d'autore, which covered literature, music, and artistic works. The system was progressive, granting authors exclusive reproduction and distribution rights, including financial benefits. It also introduced early concepts of moral rights, though these are not explicitly codified. Copyright protection lasted for the author's lifetime plus an additional period. The 1865 Code helped standardize laws during Italian unification, laying groundwork for modern copyright law, now governed by Legge 22 aprile 1941, n. 633 and EU directives.</p>

<h2>20th Century Modernization</h2>
<p>The 20th century was a decisive period for Italy, developing progressively with respect to international standards of modernity for intellectual property (IP) regulation. Notable milestones included:</p>
<p>1887: Italy joins the Berne Convention, which establishes rules for protecting literary and artistic works among member countries, and Italy commits to meeting international copyright standards.</p>
<p>Industrial Property Code (1939): This omnibus act restructured Italy's system for trademarks, patents, and industrial designs.</p>
<p>Post 2nd World War: In the immediate postwar era, Italy revamped its intellectual property laws to ensure economic recovery as well as compliance with international standards.</p>

<h2>Global Integration and Harmonization</h2>
<p>In the context of the international system, Italy has also intensified its role in the field of intellectual property through accession to the Paris Convention (1883), which structured the first international protections for industrial property. Italy participated in the foundation of WIPO (1970) in its spirit of defending creative works around the world. Moreover, Italy amended its IP laws to align with the EU, promoting harmonization in areas such as trademark and design. The European Union approved the General Copyright Directive (EU) 2019/790 in 2019. It tackles challenges of the digital age, ensuring fair compensation for creators and enhancing access to content throughout the Digital Single Market.</p>

<h2>New Developments: Industrial Property Code (CPI)</h2>
<p>The 2005 Industrial Property Code (CPI) represents a major step forward in the Italian IP landscape. It synthesized and updated existing laws within an EU and WIPO framework. The CPI covers a wide range of protections, such as trademarks and distinctive signs, geographical indications and designations of origin, designs and industrial models, patents and utility models, topographies of semiconductor products, trade secrets and new plant varieties. These protections are applicable within the national territory and are obtained through patenting, registration, or other methods specified in the CPI.</p>

<h2>How IP is Protected in Italy Today</h2>
<p>In Italy IP and therefore also copyright is protected through the SIAE, a public agency founded in 1882, born as an association it became a corporation in 1927, and it is a non-profit intermediary. Copyright is a fundamental category of natural constitutional rights that arise spontaneously at the very moment when a work of invention is created. It is important to note that these rights exist independently of any registration with the SIAE, which plays a complementary but not constitutive role.</p>
<p>The role of SIAE is mainly concerned with the practical management of copyright, acting as an intermediary in collecting the fees arising from the representation, distribution, and marketing of works. This way, authors can rely on an organized system that protects their economic interests. The relationship between authors and SIAE is a delegation: members entrust the management of their works rights to the entity, receiving in return periodic payments based on the actual use of their creations.</p>
<p>From a practical point of view, anyone who intends to organize events involving the use of registered works must necessarily obtain prior authorization from SIAE, thus guaranteeing respect for the rights of authors. One particularly important aspect of the SIAE work is the fight against piracy. The agency has developed a capillary control network throughout the country, dedicated to monitoring and preventing unauthorized releases.</p>
<p>The owner of the IP has the exclusive right to use, sell, license, or otherwise exploit the IP. In general, the person or entity who created the IP is considered the owner. However, there are some exceptions to this rule, such as when the IP is created as part of job duties or in collaboration with others.</p>

<h2>What is Not Patentable According to Art. 45 CPI?</h2>
<p><strong>General Exclusions:</strong> Discoveries, scientific theories and mathematical methods. Medical treatment methods (but products used are patentable). Plans and methods for intellectual activity, games or commerce. Software as such (protected by copyright). Presentation of information. Animal breeds and biological processes, except microbiological processes. Registered plant varieties and traditional/protected agri-food products.</p>
<p><strong>Biotechnology Exclusions:</strong> Human body and its elements. Human cloning. Human germline genetic modification. Use of human embryos. Animal genetic modifications causing unjustified suffering. Genetic screening. Aesthetic creations. Inventions against public order, morality, health and the environment.</p>
'''
    },
    'smart-contracts': {
        'title': 'Smart Contracts',
        'topic': 'Law & Tech',
        'content': """
        <h1>What is a Smart Contract</h1>

<p>
A smart contract works similarly to a traditional contract, with the key difference being that it is created on a blockchain. It is based on terms and conditions agreed upon by both parties and is written in code, often by a developer acting similarly to a legal drafter.
</p>

<p>
Once accepted, the contract executes automatically when predefined triggering conditions are met. After deployment on the blockchain, it cannot be revoked.
</p>

<h2>Blockchain</h2>

<p>
The term “smart contract” can be misleading. Despite similarities to traditional contracts, they are essentially complex sequences of “if/then” code. Initially unregulated, they are now increasingly subject to legal frameworks to ensure user protection.
</p>

<p>
Blockchain is the infrastructure that enables the transfer and execution of these codes. It is a decentralized and continuously expanding database, where no single participant has dominant control.
</p>

<p>
To maintain and expand the network, powerful computers solve complex mathematical problems in a process known as <strong>mining</strong>. This process validates new blocks added to the chain. Miners are incentivized through rewards, including cryptocurrency and, in some systems, transaction validation rights. These rewards have decreased over time due to increasing scarcity.
</p>

<p>There are two main types of blockchain consensus mechanisms:</p>

<ul>
  <li>
    <strong>Proof of Work (PoW):</strong> Used by Bitcoin, this system requires miners to solve computational problems to validate transactions and secure the network.
  </li>
  <li>
    <strong>Proof of Stake (PoS):</strong> Used by Ethereum and others, this method is more energy-efficient. Validators stake cryptocurrency and are selected (partly randomly) to validate transactions.
  </li>
</ul>

<h2>Legal Framework</h2>

<p>
As of December 18, 2017, no U.S. federal law explicitly defined the legal status of smart contracts. However, the <strong>Electronic Signatures in Global and National Commerce Act (E-Sign Act, 2000)</strong> provides a legal basis for recognizing them.
</p>

<p>
The Act establishes that electronic signatures and contracts cannot be denied legal validity solely because they are in electronic form.
</p>

<p>
Smart contracts may fall under this framework, although no explicit regulatory guidance has been issued.
</p>

<p>
In Italy, smart contracts are regulated by <strong>Law No. 12/2019</strong>.
</p>

<p>
At the EU level, regulation falls within broader categories:
</p>

<ul>
  <li><strong>DTL:</strong> Digital Technologies Law</li>
  <li><strong>AML:</strong> Anti-Money Laundering</li>
  <li><strong>CFT:</strong> Combating the Financing of Terrorism</li>
</ul>

<p>
On February 14, 2023, the European Commission launched the <strong>European Blockchain Regulatory Sandbox</strong>, aimed at reducing legal uncertainty and improving cooperation between regulators and innovators.
</p>

<p>
The <strong>Data Act</strong> (applicable from September 2025) defines a smart contract as:
</p>

<blockquote>
A computer program used for the automated execution of an agreement or part thereof, ensuring integrity and chronological accuracy of electronic data records.
</blockquote>

<p>
This implies that once agreed upon, the contract executes automatically, fully or partially.
</p>

<h2>Main Challenges</h2>

<p>
Smart contracts challenge traditional financial institutions, which have historically ensured transactional security. While the technology offers advantages—such as reducing ambiguity, bureaucracy, and bias—it also presents significant risks.
</p>

<p>
In decentralized systems, no authority can intervene during crises or defaults. Additionally, liability for coding errors remains unclear. Currently, the “rule of code” prevails over the “rule of law,” as compliance with code determines validity.
</p>

<p>
A potential solution is embedding legal principles directly into the system, either through a unified global legal framework or a shared database of legal standards capable of preventing unlawful transactions.
</p>

<h2>Credit Score Assessment</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Factor</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Payment History</td>
      <td>Track record of paying obligations on time, including defaults.</td>
    </tr>
    <tr>
      <td>Credit Utilisation</td>
      <td>Ratio of used credit to total available credit.</td>
    </tr>
    <tr>
      <td>Length of Credit History</td>
      <td>Duration of active credit accounts.</td>
    </tr>
    <tr>
      <td>Credit Mix</td>
      <td>Variety of credit types (e.g., loans, credit cards).</td>
    </tr>
    <tr>
      <td>New Credit Inquiries</td>
      <td>Frequency of recent credit applications.</td>
    </tr>
  </tbody>
</table>

<h2>Role of Statistical Data</h2>

<p>
Banks use statistical models, including logistic regression and machine learning, to predict default risk based on historical data.
</p>

<ul>
  <li>Macroeconomic indicators (e.g., unemployment, inflation)</li>
  <li>Demographic and income data</li>
  <li>Behavioral patterns (e.g., spending habits, debt levels)</li>
</ul>

<p>
Credit assessment combines individual financial behavior with predictive modeling to determine loan eligibility and risk.
</p>

<p>
Despite its potential, smart contract technology must address key limitations before widespread adoption, particularly around governance, liability, and legal integration.
</p>
        """
    },
    'buy-now-pay-later': {
        'title': 'Buy Now Pay Later',
        'topic': 'Business & Finance',
        'content': '''
<p>Buy-Now-Pay-Later is a financial solution enacted to alleviate the economic burden of the purchase of an item or service online in favor of the consumer. This new way of online payment first emerged in Europe in 2012 and later spread in the US; however, the concept is not a newcomer; in fact, the BNPL concept dates back to the 19th century, when companies and department stores offered consumers installment plans for purchasing big-ticket items like furniture, farm equipment, and other frequently out-of-budget goods. In the 1890s, Singer sewing machines popularized the “dollar down, dollar a week” payment plan. The practice consists in breaking down the total cost of the desired good/service into usually 3 or 4 monthly installments in addition to the down deposit that will be charged as soon as the purchase is validated; then the subsequent payments will be automatically processed within the agreed time span. In addition, in some cases the payment plan can also be adjusted to suit the consumer's needs.
</p>

<h2>How does it works</h2>
<p>An intermediary institution (your bank) pays upfront for the entire purchase amount. You then repay the bank through a series of fees that add up to the value of the upfront payment, typically without interest. However, if your chosen account lacks sufficient balance, penalty charges proportional to the installment amount will be triggered; thus, the higher the tranche, the higher the monetary penalty will be.
</p>

<h2>Why do they offer this ?</h2>
<p>This mechanism efficiently encourages customers to make more purchases by spreading costs over a short period. However, this system may sometimes lead consumers to make unsustainable purchases due to miscalculating or mismanaging their financial resources; in fact, the feasibility evaluation and credit score assessment of the transaction are not as thorough as in other mechanisms such as loans and mortgages; therefore, they are simplified due to the operation's rapid nature and the typical price of the goods and services provided, which are usually no more than a couple of hundred euros/dollars. In 2024, according to EMARKETER 93.3 million US consumers will use BNPL services. Users will continue to increase annually through 2027, though growth will taper due to increased competition. Though not as prevalent as debit cards (55%), credit cards (53%), or PayPal (49%), BNPL was used by 11% of US digital buyers to make a digital purchase in April 2024, according to an EMARKETER survey conducted by Bizrate Insights. As consumers look for credit card alternatives to avoid accumulating debt, BNPL has emerged as an appealing way to complete a purchase due to its ease and flexibility of use that blends the benefits of credit, short repayment terms, and app-based shopping.
</p>

<h2>Regulations</h2>
<p>BNPL services in the European Union (EU) are regulated by the Consumer Credit Directive (CCD). The CCD2 regulation, which came into force in November 2023, introduces new rules to protect consumers. On the other hand, in the US, BNPL services are regulated by the Consumer Financial Protection Bureau (CFPB) and some state governments. The CFPB has issued an interpretive rule applying credit card consumer protection rules to BNPL lenders. While some states classify BNPL as consumer credit and require state licensing or registration, others waive these requirements for BNPL products that charge no interest or finance fees. BNPL providers may also be subject to regulations governing:
Credit reporting and responsible lending practices
Advertising and marketing
Terms, fees, and interest rates
Fairness, transparency, and protection against unfair practices
'''
    },
    'predatory-lending': {
        'title': 'Predatory Lending – A Danger to Society',
        'topic': 'Business & Finance',
        'content': """
        <h1>Predatory Lending: A Danger to Society</h1>

<h2>Types of Loans</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Loan Type</th>
      <th>Collateral Required</th>
      <th>Suitable For</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Unsecured Loans</td>
      <td>No</td>
      <td>General purpose loans, no assets</td>
    </tr>
    <tr>
      <td>Secured Loans</td>
      <td>Yes</td>
      <td>Large purchases, bad credit</td>
    </tr>
    <tr>
      <td>Fixed-Rate Loans</td>
      <td>Varies</td>
      <td>Budgeting, long-term financing</td>
    </tr>
    <tr>
      <td>Variable-Rate Loans</td>
      <td>Varies</td>
      <td>Short-term loans, risk-takers</td>
    </tr>
  </tbody>
</table>

<h2>Loan Requirements in Italy</h2>
<ul>
  <li>Be over 18 years old and under 70 years old (some banks may allow older applicants).</li>
  <li>Have your place of residence in Italy. Foreigners can apply, but larger loans may require Italian citizenship.</li>
  <li>Have a stable income source.</li>
  <li>Have an Italian bank account.</li>
</ul>

<h2>Lending Money</h2>
<p>
Every natural or legal person has the right to lend money freely, at their own risk. However, due to the complexity of the operation, people prefer borrowing from intermediaries such as banks. Banks make transactions safer and easier, as licensed intermediaries can guarantee the loaned amount.
</p>

<p>
Nowadays, loan approval is less biased. Loan type, amount, and interest rate are determined by the borrower's credit score. Borrowing from a bank ensures compliance with legal requirements.
</p>

<p>
Private lending (without intermediaries) is permitted, especially if no interest is charged. However, agreements must be in writing for two main reasons:
</p>

<ol>
  <li>
    Legal protection: In case of disputes, written proof ensures enforceability of obligations and protects both creditor and debtor.
  </li>
  <li>
    Financial transparency: Helps prevent illegal practices such as money laundering or tax evasion.
  </li>
</ol>

<p>
In Italy (January–March 2018):
</p>
<ul>
  <li>Personal loans: average rate 10.2489%, usury rate 16.8111%</li>
  <li>Mortgage loans: average fixed rate 2.9380%, maximum rate 7.6725%</li>
</ul>

<h2>Payday Loans: A New Hustle or a Social Threat?</h2>

<h3>What Are Payday Loans?</h3>
<p>
A payday loan is a short-term, high-interest loan due on the borrower’s next payday. These loans target individuals needing immediate cash but often result in cycles of debt due to excessive fees and interest rates.
</p>

<p>
They are especially widespread in the United States, where approximately 12 million people use them annually, spending around $9 billion in fees. These loans are unsecured and often granted to individuals with poor credit, increasing lender risk and justifying higher interest rates.
</p>

<p>
While most states impose usury limits (typically 5%–30%), payday lenders often exploit legal exemptions. Currently, 37 states allow payday lending, though many impose restrictions or bans.
</p>

<h2>The Green Arrow Solution Case</h2>
<p>
Green Arrow Solutions (Green Arrow Loans) has been involved in multiple federal class action lawsuits in states such as Indiana, Illinois, and Massachusetts. The allegations concern loans with interest rates exceeding 700% annually, far above legal limits.
</p>

<p>
The company claims affiliation with the Big Valley Band of Pomo Indians, arguing exemption from state regulation. Plaintiffs contend this is a “rent-a-tribe” scheme, as operations are allegedly managed by non-tribal members outside tribal lands.
</p>

<p>
Dan Shaw and Greg Jones have been identified as key figures and defendants. Plaintiffs seek remedies including loan invalidation, injunctions, restitution, and damages for violations of usury and consumer protection laws.
</p>

<h2>A Matter of Efficiency?</h2>
<p>
Rising debt levels increase interest rates due to reduced trust in borrowers’ repayment capacity, widening financial inequality and shifting burdens to future generations.
</p>

<p>
Student loans illustrate this issue. Financial illiteracy and unrealistic lending expectations have led to widespread delinquency. This has triggered stricter lending requirements, limiting access to education and potentially conflicting with Article 26 of the Universal Declaration of Human Rights.
</p>

<p>
Reduced access to education may result in shortages of skilled professionals, affecting innovation, productivity, and social mobility across society.
</p>

<h2>Freedom of Contract vs Fairness</h2>
<p>
Payday loans destabilize families and can trap individuals in long-term debt. Even when legal, their social impact is largely negative.
</p>

<p>
The tension lies between fairness (borrowers often lack alternatives) and freedom of contract (individual autonomy to make financial decisions). While harmful, such transactions are difficult to prohibit without restricting personal freedom.
</p>

<h2>A Solution: “Halal” Lending</h2>
<p>
An alternative approach is the Islamic finance model based on profit-and-risk sharing rather than interest.
</p>

<ul>
  <li><strong>Murabaha:</strong> The bank purchases an asset and resells it at a fixed markup. Payments are made in installments, with no variable interest.</li>
  <li><strong>Ijara:</strong> The bank leases an asset to the customer, who gains ownership at the end of the lease.</li>
</ul>

<p>
This model ensures fair compensation for lenders while aligning incentives with borrower success. It reduces excessive debt and promotes ethical lending practices.
</p>
        """
    },
    'monopoly-of-app-store-and-apple': {
        'title': 'Monopoly of App Store and Apple',
        'topic': 'Law & Tech',
        'content': """ <h1>Monopoly of the App Store and Apple</h1>

<p>
A monopoly is a market situation where a single entity has exclusive control over a product, service, or industry. This allows it to dominate the market and influence prices and availability without competition. However, monopolies are not always forbidden. According to the Sherman Act of 1890 (US antitrust law), some monopolies are permitted.
</p>

<h2>Types of Monopoly</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Type</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Innocent Monopoly</td>
      <td>Achieved through superior business practices</td>
      <td>Google in search</td>
    </tr>
    <tr>
      <td>Natural Monopoly</td>
      <td>Single company serves the market most efficiently</td>
      <td>Historical cable companies (e.g., Comcast)</td>
    </tr>
  </tbody>
</table>

<p>
While many consumers prefer dominant products such as the iPhone or Google’s search engine, these companies have faced increasing legal challenges. In recent years, Apple Inc. lost its case regarding a €13 billion Irish tax ruling, and Google lost its challenge over a €2.4 billion fine for abuse of market dominance. These decisions represent a significant strengthening of the European Union’s enforcement against large technology companies.
</p>

<p>
The Court of Justice of the European Union confirmed in <strong>Case C-465/20 P (10 September 2024)</strong> that Ireland granted unlawful state aid to Apple. In parallel, the Court upheld findings that Google abused its dominant position by favoring its own comparison shopping service in search results.
</p>

<h2>Apple’s Business Model and Legal Challenges</h2>

<p>
Apple’s business model is built on a tightly integrated ecosystem of hardware, software, and services. While widely recognized for innovation, the company faces ongoing scrutiny regarding its App Store policies.
</p>

<p>
Due to its dominant position, Apple effectively sets the rules for app distribution on its platform. Recent changes include allowing third-party app stores and adjusting commission structures to 10–17% (down from 15–30%), plus an additional 3% fee for using Apple’s payment system.
</p>

<p>
Apple is also facing a $7 billion class action lawsuit scheduled for February 2026 in a California federal court. The claim alleges antitrust violations based on Apple’s control over app distribution, which allegedly inflates prices for consumers.
</p>

<p>
Additionally, the U.S. Department of Justice and 16 state attorneys general have raised concerns regarding Apple’s ecosystem. Key issues include:
</p>

<ul>
  <li>Restrictions on app distribution through the App Store</li>
  <li>Use of private APIs disadvantaging competitors (e.g., messaging, wearables, digital wallets)</li>
  <li>Barriers between iPhone and Android ecosystems</li>
  <li>Preferential treatment of Apple’s own services (e.g., FaceTime)</li>
</ul>

<p>
APIs (Application Programming Interfaces) are technical protocols that allow software systems to communicate. In this context, they are central to competition law because control over APIs can limit interoperability and restrict market access for competitors.
</p>

<p>
Critics argue that Apple maintains its market position through restrictive practices rather than purely through innovation, potentially reducing competition and increasing consumer costs.
</p>

<h2>Conclusion</h2>

<p>
Monopolies can arise from efficiency or innovation and may deliver consumer benefits. However, cases involving Apple and Google illustrate the increasing regulatory scrutiny applied to dominant firms.
</p>

<p>
These developments highlight the tension between encouraging innovation and preserving fair competition. The outcome of these legal challenges will significantly influence future antitrust enforcement and consumer protection in the digital economy.
</p>
        """
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/article/<slug>')
def article(slug):
    post = articles.get(slug)
    if not post:
        return "Article not found", 404
    return render_template('article.html', post=post)

@app.route('/download/cv')
def download_cv():
    return send_from_directory('static', 'cv.pdf', as_attachment=True)

@app.route('/download/portfolio')
def download_portfolio():
    return send_from_directory('static', 'portfolio.pdf', as_attachment=True)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg = Message(
        subject=f"Portfolio Contact: {subject}",
        sender=os.getenv('MAIL_USERNAME'),
        recipients=[os.getenv('MAIL_USERNAME')]
    )
    msg.body = f"From: {name} <{email}>\n\n{message}"

    try:
        mail.send(msg)
        flash('Message sent successfully!', 'success')
    except:
        flash('Something went wrong. Please try again.', 'error')

    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)