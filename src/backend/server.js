const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Dummy data for demonstration purposes
let projects = [
    {
        id: 1,
        title: '【急募・長期案件】不動産査定SaaSのAI自動化・Rails開発エンジニア募集',
        description: 'プロジェクト概要...',
        status: 'open'
    }
];

// API routes
app.get('/projects', (req, res) => {
    res.json(projects);
});

app.get('/projects/:id', (req, res) => {
    const project = projects.find(p => p.id === parseInt(req.params.id));
    if (!project) return res.status(404).send('Project not found');
    res.json(project);
});

app.post('/projects', (req, res) => {
    const newProject = {
        id: projects.length + 1,
        title: req.body.title,
        description: req.body.description,
        status: 'open'
    };
    projects.push(newProject);
    res.status(201).json(newProject);
});

app.put('/projects/:id', (req, res) => {
    const project = projects.find(p => p.id === parseInt(req.params.id));
    if (!project) return res.status(404).send('Project not found');

    project.title = req.body.title;
    project.description = req.body.description;
    project.status = req.body.status;

    res.json(project);
});

app.delete('/projects/:id', (req, res) => {
    const projectIndex = projects.findIndex(p => p.id === parseInt(req.params.id));
    if (projectIndex === -1) return res.status(404).send('Project not found');

    projects.splice(projectIndex, 1);
    res.json({ message: 'Project deleted' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});